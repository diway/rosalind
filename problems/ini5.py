input = open('input_filename', 'r')
even_lines = input.readlines()[1::2]
output = open('output_filename', 'w')
output.writelines(even_lines)
input.close()
output.close()
