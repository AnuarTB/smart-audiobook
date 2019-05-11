from deeppavlov import build_model, configs

model = build_model(configs.squad.squad, download=False)
#model.save()
print(model(['DeepPavlov is library for NLP and dialog systems.'], ['What is DeepPavlov?']))

def answer(text, question):
    return model([text], [question])