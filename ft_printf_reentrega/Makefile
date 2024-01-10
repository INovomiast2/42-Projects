NAME = libftprintf.a
FLAGS = -Wall -Werror -Werror

FILES = ft_printf.c \
	   	ft_printf_utils.c \
		ft_printf_print.c

OBJS = $(FILES:.c=.o)

all: $(NAME)

$(NAME): $(OBJS)
	ar rc $(NAME) $(OBJS)
	ranlib $(NAME)
	@echo "\033[0;32m$(NAME) created successfully!\033[0m"

$(OBJS): $(FILES)
	gcc $(FLAGS) -c $(FILES)

clean:
	rm -f $(OBJS)

fclean: clean
	rm -f $(NAME)
	@echo "\033[0;32m$(NAME) cleaned successfully!\033[0m"

re: fclean all

.PHONY = all clean fclean re