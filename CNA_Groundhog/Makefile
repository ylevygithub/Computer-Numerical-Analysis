##
## EPITECH PROJECT, 2020
## make
## File description:
## make
##

SRC =   $(wildcard src/*.cpp)

OBJ =   $(SRC:.cpp=.o)

NAME    =   groundhog

$(NAME):    $(OBJ)
	g++ -I src/ -o $(NAME) $(OBJ)

all:    $(NAME)

clean:
	rm -f $(OBJ)

fclean: clean
	rm -f $(NAME)

re: fclean all
