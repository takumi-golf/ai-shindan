from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = T5ForConditionalGeneration.from_pretrained("sonoisa/t5-base-japanese").to(device)
tokenizer = T5Tokenizer.from_pretrained("sonoisa/t5-base-japanese")

def generate_questions(context: str, num_questions=5):
    input_text = f"質問生成: {context}"
    inputs = tokenizer(input_text, return_tensors="pt").to(device)
    outputs = model.generate(
        inputs.input_ids,
        max_length=512,
        num_return_sequences=num_questions
    )
    return [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
