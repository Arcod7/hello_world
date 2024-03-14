##
## EPITECH PROJECT, 2024
## ImageCompressor
## File description:
## Makefile
##

NAME	=	hello_world

SRC	=	main.c

OBJ	=	$(SRC:.c=.o)

all: $(OBJ)
	gcc -o $(NAME) $(OBJ)

clean:
	rm *.o

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re
