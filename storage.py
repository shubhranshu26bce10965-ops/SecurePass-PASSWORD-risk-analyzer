def save_result(password, score, risk):
    file = open("history.txt", "a")

    file.write("Password : " + password + "\n")
    file.write("Score    : " + str(score) + "\n")
    file.write("Risk     : " + risk + "\n")
    file.write("--------------------------\n")

    file.close()

def view_history():
    file = open("history.txt", "r")
    data = file.read()
    file.close()
    return data
