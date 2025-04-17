from flask import Flask, render_template, request
import openai
from dotenv import load_dotenv
import os
import requests
import time
from concurrent.futures import ThreadPoolExecutor

# 加载环境变量
load_dotenv()
app = Flask(__name__)

# DeepSeek配置
openai.api_key = os.getenv("DEEPSEEK_API_KEY")
openai.api_base = "https://api.deepseek.com/v1"

# 图像风格选项映射
STYLE_MAP = {
    "realistic": "hyper-realistic photography",
    "cartoon": "vibrant cartoon illustration",
    "watercolor": "delicate watercolor painting",
    "cyberpunk": "neon-lit cyberpunk style",
    "minimalism": "minimalist design"
}

def call_deepseek(prompt, max_retries=2):
    """封装DeepSeek API调用"""
    for attempt in range(max_retries):
        try:
            response = openai.ChatCompletion.create(
                model="deepseek-chat",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=500
            )
            return response['choices'][0]['message']['content'].strip()
        except Exception as e:
            if attempt == max_retries - 1:
                return f"生成失败：{str(e)}"
            time.sleep(1)

def generate_image_prompt(form_data):
    """生成图像提示词"""
    prompt_template = f"""
    作为专业广告设计师，请为 {form_data['product']} 生成图像提示词：
    - 产品描述：{form_data['description']}
    - 目标受众：{form_data['audience']}
    - 风格要求：{STYLE_MAP.get(form_data['art_style'], '专业风格')}
    - 构图类型：{form_data['composition']}
    - 必须使用英文
    输出格式：<视觉描述>, <构图方式>, <色彩方案>"""
    
    return call_deepseek(prompt_template)

def generate_copywriting(form_data):
    """生成广告文案"""
    prompt = f"""
    撰写广告文案：
    产品：{form_data['product']}
    描述：{form_data['description']}
    受众：{form_data['audience']}
    语气：{form_data['tone']}
    平台：{form_data['platform']}
    要求：2-3句话，必须使用英文，包含吸引眼球的标题"""
    
    return call_deepseek(prompt)

def generate_image(image_prompt):
    """生成图片"""
    try:
        response = requests.post(
            "https://api.deepai.org/api/text2img",
            data={'text': image_prompt},
            headers={'api-key': os.getenv("DEEPAI_API_KEY")},
            timeout=20
        )
        if response.status_code == 200:
            return response.json().get('output_url')
    except Exception as e:
        print(f"图像生成错误：{str(e)}")
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        start_time = time.time()
        form_data = {
            'product': request.form['product'],
            'description': request.form['description'],
            'audience': request.form['audience'],
            'tone': request.form['tone'],
            'platform': request.form['platform'],
            'art_style': request.form.get('art_style', 'realistic'),
            'composition': request.form.get('composition', 'close-up')
        }

        # 第一步：生成图像提示词
        image_prompt = generate_image_prompt(form_data)
        if "失败" in image_prompt:
            return render_template("error.html", message=image_prompt)

        # 第二步：并行生成文案和图片
        with ThreadPoolExecutor() as executor:
            copy_future = executor.submit(generate_copywriting, form_data)
            image_future = executor.submit(generate_image, image_prompt)
            
            ad_copy = copy_future.result()
            image_url = image_future.result()

        return render_template("result.html",
                            ad_copy=ad_copy,
                            image_url=image_url,
                            image_prompt=image_prompt,
                            elapsed_time=round(time.time()-start_time, 2))

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)