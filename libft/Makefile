NAME = libft.a

FLAGS = -Wall -Wextra -Werror

FILES = ft_isalpha.c\
		ft_isdigit.c\
		ft_isalnum.c\
		ft_isascii.c\
		ft_isprint.c\
		ft_strlen.c\
		ft_memset.c\
		ft_bzero.c\
		ft_memcpy.c\
		ft_memmove.c\

OBJS = $(FILES:.c=.o)

all: $(NAME)

$(NAME): $(OBJS)
	ar rc $(NAME) $(OBJS)

$(OBJS): $(FILES)
	gcc $(FLAGS) -c $(FILES)

clean:
	rm -f $(OBJS) $(OBJS_BONUS)
	
fclean:
	rm -f $(NAME) $(OBJS) $(OBJS_BONUS)

re : fclean all

.PHONY: all clean fclean re
