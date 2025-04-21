#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int nombreAleatori;

    // Inicialitza la llavor del generador de nombres aleatoris amb el temps actual
    srand(time(NULL));

    // Genera un nombre aleatori entre 0 i 99
    nombreAleatori = rand() % 100;

    // Imprimeix el nombre aleatori
    printf("El nombre aleatori generat és: %d\n", nombreAleatori);

    return 0;
}
