from flask import Flask, render_template, jsonify, request
import openai

api_key = "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"
app = Flask(__name__)
client = openai.Client(api_key=api_key)
thread = client.beta.threads.create()

math = client.beta.assistants.create(
    name='Mathematics Tutor',
    instructions='You are a mathematics tutor and dont answer anything outsdide mathematics',    tools=[],
    model='gpt-3.5-turbo-1106'
)
phy = client.beta.assistants.create(
    name='Physics Tutor',
    instructions='You are a physics tutor and dont answer anything outsdide physics',
    tools=[],
    model='gpt-3.5-turbo-1106'
)
che = client.beta.assistants.create(
    name='Chemistry Tutor',
    instructions='You are a chemistry tutor and dont answer anything outsdide chemistry',
    tools=[],
    model='gpt-3.5-turbo-1106'
)
bio = client.beta.assistants.create(
    name='Biology Tutor',
    instructions='You are a biology tutor and dont answer anything outsdide biology',
    tools=[],
    model='gpt-3.5-turbo-1106'
)
eng = client.beta.assistants.create(
    name='English Tutor',
    instructions='You are a english language tutor and dont answer anything outsdide english language',
    tools=[],
    model='gpt-3.5-turbo-1106'
)
arb = client.beta.assistants.create(
    name='Arabic Tutor',
    instructions='You are a arabic language grammers tutor and dont answer anything outsdide arabic language',
    tools=[],
    model='gpt-3.5-turbo-1106'
)


def askmath(q):
    message = client.beta.threads.messages.create(thread_id=thread.id, role='user', content=q)

    run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=math.id)

    while True:
        run_status = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        if run_status.completed_at is not None:
            break
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    response = []
    for i in messages.data:
        if i.role == 'assistant':
            for c in i.content:
                if c.type == 'text':
                    response.append(c.text.value)
    return response[0]

def askphy(q):
    message = client.beta.threads.messages.create(thread_id=thread.id, role='user', content=q)

    run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=phy.id)

    while True:
        run_status = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        if run_status.completed_at is not None:
            break
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    response = []
    for i in messages.data:
        if i.role == 'assistant':
            for c in i.content:
                if c.type == 'text':
                    response.append(c.text.value)
    return response[0]

def askche(q):
    message = client.beta.threads.messages.create(thread_id=thread.id, role='user', content=q)

    run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=che.id)

    while True:
        run_status = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        if run_status.completed_at is not None:
            break
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    response = []
    for i in messages.data:
        if i.role == 'assistant':
            for c in i.content:
                if c.type == 'text':
                    response.append(c.text.value)
    return response[0]

def askbio(q):
    message = client.beta.threads.messages.create(thread_id=thread.id, role='user', content=q)

    run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=bio.id)

    while True:
        run_status = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        if run_status.completed_at is not None:
            break
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    response = []
    for i in messages.data:
        if i.role == 'assistant':
            for c in i.content:
                if c.type == 'text':
                    response.append(c.text.value)
    return response[0]

def askeng(q):
    message = client.beta.threads.messages.create(thread_id=thread.id, role='user', content=q)

    run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=eng.id)

    while True:
        run_status = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        if run_status.completed_at is not None:
            break
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    response = []
    for i in messages.data:
        if i.role == 'assistant':
            for c in i.content:
                if c.type == 'text':
                    response.append(c.text.value)
    return response[0]

def askarb(q):
    message = client.beta.threads.messages.create(thread_id=thread.id, role='user', content=q)

    run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=arb.id)

    while True:
        run_status = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        if run_status.completed_at is not None:
            break
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    response = []
    for i in messages.data:
        if i.role == 'assistant':
            for c in i.content:
                if c.type == 'text':
                    response.append(c.text.value)
    return response[0]

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    question = request.json['question']
    tutor = request.json['tutor']
    if tutor == 'math':
        return jsonify({'answer': askmath(question)})
    if tutor == 'phy':
        return jsonify({'answer': askphy(question)})
    if tutor == 'che':
        return jsonify({'answer': askche(question)})
    if tutor == 'bio':
        return jsonify({'answer': askbio(question)})
    if tutor == 'eng':
        return jsonify({'answer': askeng(question)})
    if tutor == 'arb':
        return jsonify({'answer': askarb(question)})


if __name__ == '__main__':
    app.run(debug=True,port=3001)