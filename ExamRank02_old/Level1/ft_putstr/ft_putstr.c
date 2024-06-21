#include <unistd.h>

void    ft_putstr(char *str)
{
    int i = -1;

    while (str[++i])
        write(1, &str[i], 1);
}

int main(void)
{
    ft_putstr("Soy guapa, soy lista. \n");
    ft_putstr("Y salgo en la revista.");
    return (0);
}