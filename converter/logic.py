def convert_to_test_case(user_story):
    if not user_story.strip():
        return "Please enter a valid user story."

    test_case = "Test Case:\n"

    if "As a" in user_story and "I want" in user_story and "so that" in user_story:
        parts = user_story.split("so that")
        goal = parts[1].strip().capitalize()
        role_action = parts[0].split("I want")
        role = role_action[0].replace("As a", "").strip()
        action = role_action[1].strip().capitalize()

        test_case += f"Title: {action}\n"
        test_case += f"Role: {role}\n"
        test_case += f"Precondition: {role} is logged in (if required)\n"
        test_case += f"Action: {action}\n"
        test_case += f"Expected Result: {goal}\n"
    else:
        test_case = "Unsupported format. Use: 'As a [role], I want [action] so that [goal]'."

    return test_case