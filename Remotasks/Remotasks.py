# ## response 1

# #!What exactly is wrong with my code?

# import pygame
# import random

# pygame.init()

# screen_width = 600
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Snake Game")

# black = (0, 0, 0)
# white = (255, 255, 255)
# green = (0, 255, 0)
# red = (255, 0, 0)

# snake_block = 10
# snake_speed = 15

# snake_x = screen_width / 2
# snake_y = screen_height / 2

# snake_list = []
# snake_length = 1

# food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
# food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

# game_over = False

# while not game_over:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             game_over = True
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 snake_x_change = -snake_block
#                 snake_y_change = 0
#             elif event.key == pygame.K_RIGHT:
#                 snake_x_change = snake_block
#                 snake_y_change = 0
#             elif event.key == pygame.K_UP:
#                 snake_y_change = -snake_block
#                 snake_x_change = 0
#             elif event.key == pygame.K_DOWN:
#                 snake_y_change = snake_block
#                 snake_x_change = 0

#     snake_x += snake_x_change
#     snake_y += snake_y_change

#     snake_head = []
#     snake_head.append(snake_x)
#     snake_head.append(snake_y)
#     snake_list.append(snake_head)
#     if len(snake_list) > snake_length:
#         del snake_list[0]

#     if snake_x == food_x and snake_y == food_y:
#         food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
#         food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
#         snake_length += 1

#     if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
#         game_over = True

#     for x in snake_list[:-1]:
#         if x == snake_head:
#             game_over = True

#     screen.fill(black)
#     for pos in snake_list:
#         pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], snake_block, snake_block))
#     pygame.draw.rect(screen, red, pygame.Rect(food_x, food_y, snake_block, snake_block))

#     pygame.display.update()

#     pygame.time.delay(snake_speed)

# pygame.quit()


# import pygame
# import random

# pygame.init()

# screen_width = 600
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Snake Game")

# black = (0, 0, 0)
# white = (255, 255, 255)
# green = (0, 255, 0)
# red = (255, 0, 0)

# snake_block = 10
# snake_speed = 15

# snake_x = screen_width / 2
# snake_y = screen_height / 2

# snake_list = []
# snake_length = 1
# #! this here
# snake_x_change = 0
# snake_y_change = 0

# food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
# food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

# game_over = False

# while not game_over:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             game_over = True
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 snake_x_change = -snake_block
#                 snake_y_change = 0
#             elif event.key == pygame.K_RIGHT:
#                 snake_x_change = snake_block
#                 snake_y_change = 0
#             elif event.key == pygame.K_UP:
#                 snake_y_change = -snake_block
#                 snake_x_change = 0
#             elif event.key == pygame.K_DOWN:
#                 snake_y_change = snake_block
#                 snake_x_change = 0

#     snake_x += snake_x_change
#     snake_y += snake_y_change

#     snake_head = []
#     snake_head.append(snake_x)
#     snake_head.append(snake_y)
#     snake_list.append(snake_head)
#     if len(snake_list) > snake_length:
#         del snake_list[0]

#     if snake_x == food_x and snake_y == food_y:
#         food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
#         food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
#         snake_length += 1

#     if (
#         snake_x >= screen_width
#         or snake_x < 0
#         or snake_y >= screen_height
#         or snake_y < 0
#     ):
#         game_over = True

#     for x in snake_list[:-1]:
#         if x == snake_head:
#             game_over = True

#     screen.fill(black)
#     for pos in snake_list:
#         pygame.draw.rect(
#             screen, green, pygame.Rect(int(pos[0]), int(pos[1]), snake_block, snake_block)
#         )
#     pygame.draw.rect(screen, red, pygame.Rect(int(food_x), int(food_y), snake_block, snake_block))

#     pygame.display.update()

#     pygame.time.delay(snake_speed)

# pygame.quit()

###!
# import numpy as np

# def normalize_data(data):
#     data = (data - mean(data)) / std(data)
#     return data

# def split_data(data, train_size=0.7, val_size=0.1):
#     train_size, val_size, test_size = train_size, val_size, 1 - (train_size + val_size)

#     train_data = data[:int(train_size * len(data))]
#     val_data = data[int(train_size * len(data)):int((train_size + val_size) / len(data))]
#     test_data = data[int((train_size - val_size) * len(data)):]

#     return train_data, val_data, test_data

# data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# !
# train_data, val_data, test_data = split_data(normalize_data(data))

# print(f"Train data: {train_data}")
# print(f"Validation data: {val_data}")
# print(f"Test data: {test_data}")
#!GPT
# #what is wrong with this code?
'''
There is an issue in the split_data function where the
slicing is incorrect, and the calculation of validation
data is not accurate. Additionally, the normalization
should be applied separately to the training, validation,
 and test sets after splitting the data.
'''
# import numpy as np

# def normalize_data(data):
#     # Calculate mean and standard deviation for normalization
#     mean_value = np.mean(data)
#     std_value = np.std(data)

#     # Apply normalization
#     normalized_data = (data - mean_value) / std_value
#     return normalized_data

# def split_data(data, train_size=0.7, val_size=0.1):
#     train_size, val_size, test_size = train_size, val_size, 1 - (train_size + val_size)

#     # Calculate indices for slicing
#     train_end = int(train_size * len(data))
#     val_end = train_end + int(val_size * len(data))

#     # Correct slicing for train, validation, and test sets
#     train_data = data[:train_end]
#     val_data = data[train_end:val_end]
#     test_data = data[val_end:]

#     return train_data, val_data, test_data

# # Original data
# data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# #! Apply normalization before splitting
# normalized_data = normalize_data(data)

# # Corrected splitting after normalization
# train_data, val_data, test_data = split_data(normalized_data)

# # Print the results
# print(f"Train data: {train_data}")
# print(f"Validation data: {val_data}")
# print(f"Test data: {test_data}")





# import numpy as np

# def normalize_data(data):
#     data = (data - np.mean(data)) / np.std(data)
#     return data

# def split_data(data, train_size=0.7, val_size=0.1):
#     train_size, val_size, test_size = train_size, val_size, 1 - (train_size + val_size)

#     train_data = data[:int(train_size * len(data))]
#     val_data = data[int(train_size * len(data)):int((train_size + val_size) * len(data))]
#     test_data = data[int((train_size + val_size) * len(data)):]

#     return train_data, val_data, test_data

# data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# train_data, val_data, test_data = split_data(normalize_data(data))

# print(f"Train data: {train_data}")
# print(f"Validation data: {val_data}")
# print(f"Test data: {test_data}")


# import numpy as np

# def normalize_data(data):
#     data = (data - mean(data)) / std(data)
#     return data

# def split_data(data, train_size=0.7, val_size=0.1):
#     train_size, val_size, test_size = train_size, val_size, 1 - (train_size + val_size)

#     train_data = data[:int(train_size * len(data))]
#     val_data = data[int(train_size * len(data)):int((train_size + val_size) / len(data))]
#     test_data = data[int((train_size - val_size) * len(data)):]

#     return train_data, val_data, test_data

# data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# train_data, val_data, test_data = split_data(normalize_data(data))

# print(f"Train data: {train_data}")
# print(f"Validation data: {val_data}")
# print(f"Test data: {test_data}")
##!!!!!!

# def calculate_grades(grades):

#     # Type checking and handling edge cases
#     if not isinstance(grades, list):
#         return "Input should be a list"
#     if len(grades) == 0:
#         return "The grade list cannot be empty"
#     try:
#         # casting all elements to float
#         grades = [float(i) for i in grades]
#     except ValueError:
#         return "List should only contain numerical grades"

#     # Calculate average
#     summation = sum(grades)
#     num_grades = len(grades)
#     average = round(summation/num_grades, 2)

#     # Get highest and lowest grades
#     highest_grade = max(grades)
#     lowest_grade = min(grades)

#     response = {
#         'average': average,
#         'highest': highest_grade,
#         'lowest': lowest_grade,
#     }

#     return response
# # nums =[]
# # nums = ['45.45677','5','6','7']
# # nums = ['t','r']
# nums = [45.45677,5,6,7]
# # nums = 8
# print (calculate_grades(nums))

#!!!!
'''
I'm trying to initialize a list of points in python where the y coordinate is double the x
coordinate and the x coordinate is increasing from 0 to 5. Please tell me what I'm doing wrong:
'''
#! response 1
# o = {"x": 0, "y": 0}
# l = []
# for i in range(6):
#   m = o.copy()
#   m["x"] = i
#   m["y"] = i * 2
#   l.append(m)
# print(l)
#! response 2
# l = []
# for i in range(6):
#   m = {"x": i, "y": i * 2}
#   l.append(m)
# print()
##!!!!!!!
'''
Create a python program that is a typing speed test simulator on command line.
 Have the user type a predefined paragraph then when they press enter, tally the typing speed.
'''

# import time

# # Predefined paragraph
# text = "This is a paragraph for you to type. It has a variety of words and punctuation. Ready, set, go!"

# print(text)  # Display the text

# # Start the timer
# start_time = time.time()

# # Get user input
# user_input = input("Type the paragraph and press Enter: ")

# # End the timer
# end_time = time.time()

# # Calculate the time taken
# time_taken = end_time - start_time

# # Calculate words per minute (WPM)
# wpm = len(user_input.split()) / time_taken * 60

# # Print the results
# print("Your typing speed is:", wpm, "words per minute.")



# import time

# def typing_test(paragraph):
#     """Prompts the user to type the given paragraph and records their time."""

#     print("Ready to start the typing test? Press Enter to begin.")
#     input()  # Wait for user to press Enter

#     start_time = time.time()
#     user_input = input(paragraph)  # Display paragraph and prompt user to type

#     end_time = time.time()
#     time_taken = end_time - start_time

#     return user_input, time_taken

# def calculate_wpm(paragraph, time_taken):
#     """Calculates the typing speed in words per minute."""

#     words = len(paragraph.split())  # Count words in the paragraph
#     words_per_minute = (words / time_taken) * 60

#     return round(words_per_minute, 2)

# if __name__ == "__main__":
#     paragraph = "This is a sample paragraph for the typing speed test. It contains a variety of words and sentence lengths to assess your typing accuracy and speed."

#     user_input, time_taken = typing_test(paragraph)
#     wpm = calculate_wpm(paragraph, time_taken)

#     print("\nTyping Speed:", wpm, "words per minute")
#!!!!!
# def imaginaryString():

#                 arr_1 = ['X', 'V', 'D', 'E', 'L', 'W', 'P', 'M', 'Q', 'J']
#                 arr_2 = ['X', 'F', 'D', 'R', 'G', 'C', 'Y', 'E', 'O', 'B']

#                 arr_3 = get_common_values (arr_1, arr_2)
#                 arr_3 = sort_ascending (arr_3)

#                 a = [0, 1, 2]
#                 i = 0

#                 while (i < len(arr_3)):

#                         print (arr_3[ a[i] ])
#                         i = i + 1
# def imaginaryString():
#     arr_1 = ['X', 'V', 'D', 'E', 'L', 'W', 'P', 'M', 'Q', 'J']
#     arr_2 = ['X', 'F', 'D', 'R', 'G', 'C', 'Y', 'E', 'O', 'B']

#     arr_3 = get_common_values(arr_1, arr_2)
#     arr_3 = sort_ascending(arr_3)

#     for i in range(3):
#         print(arr_3[i])

# def get_common_values(arr1, arr2):
#     return list(set(arr1) & set(arr2))

# def sort_ascending(arr):
#     return sorted(arr)

# imaginaryString()

# def imaginaryString():
#     arr_1 = ['X', 'V', 'D', 'E', 'L', 'W', 'P', 'M', 'Q', 'J']
#     arr_2 = ['X', 'F', 'D', 'R', 'G', 'C', 'Y', 'E', 'O', 'B']

#     arr_3 = get_common_values(arr_1, arr_2)
#     arr_3 = sort_ascending(arr_3)

#     a = [0, 1, 2]
#     i = 0

#     while i < len(arr_3):  # Fix: 'length' should be changed to 'len'
#         print(arr_3[a[i]])  # Fix: Add parentheses for the print function
#         i += 1  # Fix: Use the shorthand for incrementing i

# # Placeholder functions for get_common_values and sort_ascending
# def get_common_values(arr1, arr2):
#     return list(set(arr1) & set(arr2))

# def sort_ascending(arr):
#     return sorted(arr)

# # Calling the imaginaryString function
# imaginaryString()
#! !!!!!!!!!

# from PIL import Image

# # Open an image file
# image = Image.open('path/to/your/image.jpg')

# # Get the dimensions of the image
# width, height = image.size

# # Create a new empty image with the same size as the original
# grayscale_image = Image.new('L', (width, height))

# # Convert the image to grayscale using nested for loops
# for x in range(width):
#     for y in range(height):
#         # Get the RGB pixel value at the current location
#         pixel = image.getpixel((x, y))

#         # Calculate the grayscale value (average of RGB channels)
#         gray_value = int(sum(pixel) / 3)

#         # Set the grayscale pixel value in the new image
#         grayscale_image.putpixel((x, y), gray_value)

# # Save the grayscale image
# grayscale_image.save('grayscale_example.jpg')

# # Display the grayscale image
# grayscale_image.show()
print(bool([]))
