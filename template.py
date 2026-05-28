import time
from openai import OpenAI

client = OpenAI(api_key="api key")

prompt = "Hãy kể cho tôi một sự thật thú vị về Việt Nam."

print("=" * 60)
print("BÀI 2.1 — THÍ NGHIỆM TEMPERATURE (gpt-4o)")
print("=" * 60)
for temp in [0.0, 0.5, 1.0, 1.5]:
    start = time.time()
    r = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=temp, top_p=0.9, max_tokens=256,
    )
    latency = time.time() - start
    text = r.choices[0].message.content
    tokens = r.usage.completion_tokens
    print(f"\n--- TEMPERATURE {temp} | latency: {latency:.2f}s | tokens: {tokens} ---")
    print(text)

print("\n" + "=" * 60)
print("SO SÁNH GPT-4o vs GPT-4o-mini")
print("=" * 60)
for model in ["gpt-4o", "gpt-4o-mini"]:
    start = time.time()
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7, top_p=0.9, max_tokens=256,
    )
    latency = time.time() - start
    text = r.choices[0].message.content
    tokens = r.usage.completion_tokens
    print(f"\n--- {model} | latency: {latency:.2f}s | tokens: {tokens} ---")
    print(text)