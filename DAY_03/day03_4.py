
def read_line(file_context, count):
    return count + 1, file_context.readline()

is_reading_file = True
counter = 0
with open('./test_case') as data:
    counter, upper_line = read_line(data, counter)
    counter, middle_line = read_line(data, counter)
    counter, lower_line = read_line(data, counter)
    while is_reading_file:






        upper_line = lower_line
        counter =+ 1
        counter, middle_line = read_line(data, counter)
        counter, lower_line = read_line(data, counter)








