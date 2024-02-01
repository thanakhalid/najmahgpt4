from django.shortcuts import render
import openai

# View for displaying the quiz form
def quiz_form(request):
    return render(request, 'templates/quizapp/quiz_form.html')

# View for generating and displaying the quiz
def generate_quiz(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        openai.api_key = 'your-api-key'

        response = openai.ChatCompletion.create(
            model="gpt-4.0-turbo",
            messages=[
                {"role": "user", "content": f"Create a quiz based on the following text: {text}"}
            ]
        )
        
        quiz_questions = response.choices[0].message['content']
        # Render the quiz display template with the generated questions
        return render(request, 'templates/quizapp/quiz_display.html', {'quiz_questions': quiz_questions})
    else:
        # Redirect back to the quiz form if it's not a POST request
        return render(request, 'templates/quizapp/quiz_form.html')
