import os
from fastapi import FastAPI, Request
from transformers import MT5Tokenizer, MT5ForConditionalGeneration, pipeline

model_path = os.environ.get('MODEL_PATH')
tokenizer = MT5Tokenizer.from_pretrained(model_path)
model = MT5ForConditionalGeneration.from_pretrained(model_path)
generator = pipeline("text2text-generation", model=model.eval(), tokenizer=tokenizer)

app = FastAPI()

@app.post("/predict")
async def predict(request: Request):
    data = await request.body()
    data_str = data.decode("utf-8") 

    outputs = generator(
        "translate French to English: " + data_str,
        max_length=128,
        do_sample=True,
        temperature=0.4
    )
    return outputs
