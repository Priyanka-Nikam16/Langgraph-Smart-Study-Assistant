from app.graph import graph

def run ():
    print("Smart study assistant")

    while True:
        question=input("Enter your question(or 'exit' to quit)")
        if question.lower()== 'exit':
            break
        # Here we will process the question
        print(f"You asked :,{question}")
        result=graph.invoke(
            {
                "question": question,
                "question_type":"",
                "answer":""})
        print("\n\n")
        print(f"Question type which you have asked:{result['question_type']}")
        print("\n\n")
        print(f"Answer:,{result['answer']}")

if __name__=="__main__":
    run()