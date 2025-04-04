from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch

# デバイス設定（GPUが利用可能ならGPU、それ以外はCPU）
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# モデルとトークナイザーの初期化
model = T5ForConditionalGeneration.from_pretrained(
    "sonoisa/t5-base-japanese",
    force_download=True  # resume_download を置き換え
).to(device)

tokenizer = T5Tokenizer.from_pretrained("sonoisa/t5-base-japanese")

def generate_questions(context: str, num_questions=5):
    """
    質問文生成関数

    Args:
        context (str): 質問生成のコンテキスト。
        num_questions (int): 生成する質問数。

    Returns:
        list: 生成された質問文リスト。
    """
    input_text = f"質問生成:{context}"
    inputs = tokenizer(input_text, return_tensors="pt").to(device)
    
    outputs = model.generate(
        inputs.input_ids,
        max_length=64,               # 出力トークン数制限
        num_beams=6,                 # ビームサーチ幅
        num_return_sequences=num_questions,
        no_repeat_ngram_size=2,      # N-gram繰り返し防止
        early_stopping=True          # 早期終了有効化
    )
    
    return [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
