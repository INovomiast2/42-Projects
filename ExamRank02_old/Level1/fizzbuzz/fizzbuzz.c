#include <unistd.h>

void    ft_putchar(char c)
{
    write(1, &c, 1);
}

void    ft_putstr(char *str)
{
    int i = -1;

    while (str[++i])
        ft_putchar(str[i]);
}

void    ft_putnbr(int nbr)
{
    char *str = "0123456789";

    if (nbr > 9)
    {
        ft_putnbr(nbr / 10);        
    }
    write(1, &str[nbr % 10], 1);
}

int main(void)
{
    int i = 0;

    while (i <= 100)
    {
        if (i % 3 == 0)
            ft_putstr("fizz");
        else if (i % 5 == 0)
            ft_putstr("buzz");
        else if (i % 15 == 0)
            ft_putstr("fizzbuzz");
        else
            ft_putnbr(i);
        ft_putchar('\n');
        i++;
    }
    return (0);
}