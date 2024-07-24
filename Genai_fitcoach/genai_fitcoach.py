import streamlit as st
import google.generativeai as genai

# Initialize Generative AI with your API key
api_key = 'AIzaSyBNIPek28Vah9dQAPTIsXBgWAV5_LDO3ao'  # Replace with your actual API key
genai.configure(api_key=api_key)

# Function to generate workout plan using Generative AI based on user input
def generate_workout_plan(goal, fitness_level, duration):
    try:
        prompt = f"Create a {duration}-month workout plan for a {fitness_level} level individual aiming to {goal}. Provide a detailed plan including exercises, sets, and reps for each month."
        response = genai.generate_text(prompt=prompt)
        
        # Extract result from the response
        if response and hasattr(response, 'result'):
            return response.result
        else:
            return "No workout plan generated."
    except Exception as e:
        st.error(f"An error occurred generating workout plan: {e}")
        return None

# Function to generate fitness tips using Generative AI based on user input
def generate_fitness_tips(topic):
    try:
        prompt = f"Provide fitness tips on {topic}."
        response = genai.generate_text(prompt=prompt)
        
        # Extract result from the response
        if response and hasattr(response, 'result'):
            return response.result
        else:
            return "No fitness tips generated."
    except Exception as e:
        st.error(f"An error occurred generating fitness tips: {e}")
        return None

# Main function for Streamlit app
def main():
    st.markdown("<h1 style='color: green;'>GenAI FitCoach</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: #0089FF;'>🏋️‍♂️ Your Personalized AI Fitness Coach</h2>", unsafe_allow_html=True)
    
    st.markdown("""
        <p>Welcome to GenAI FitCoach! This app uses Generative AI to create customized workout plans and provide fitness tips tailored to your needs.</p>
    """, unsafe_allow_html=True)

    st.markdown("### Generate Workout Plan")
    goal = st.selectbox("Select your fitness goal", ["Lose Weight", "Build Muscle", "Improve Endurance"])
    fitness_level = st.selectbox("Select your fitness level", ["Beginner", "Intermediate", "Advanced"])
    duration = st.slider("Select duration of the workout plan (months)", 1, 12, 3)
    generate_plan_button = st.button("Generate Workout Plan")

    if generate_plan_button:
        workout_plan = generate_workout_plan(goal, fitness_level, duration)
        if workout_plan:
            st.success("Your Workout Plan:")
            st.write(workout_plan)
        else:
            st.warning("Failed to generate workout plan. Please try again.")

    st.markdown("### Get Fitness Tips")
    topic = st.text_input("Enter a topic for fitness tips (e.g., nutrition, recovery, etc.)")
    generate_tips_button = st.button("Generate Fitness Tips")

    if generate_tips_button and topic:
        fitness_tips = generate_fitness_tips(topic)
        if fitness_tips:
            st.success("Fitness Tips:")
            st.write(fitness_tips)
        else:
            st.warning("Failed to generate fitness tips. Please try again.")

if __name__ == '__main__':
    main()
