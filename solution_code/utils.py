def get_test_input(folder):
    with open('./../input_data/' + folder + '/test_input.txt', 'r') as file:
        return file.read()
    
def write_solution(folder, part, answer):
    with open('./../submitted_answers/' + folder + '/answer_' + part, 'w') as file:
        file.write(answer)