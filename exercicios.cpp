#include <iostream>

using namespace std;

void exercicio1();
//void exercicio2();
//void exercicio3();

int main() {

    exercicio1();
    //exercicio2();
    //exercicio3();

    return 0;
}

void exercicio1() {
    double notas[3] = {0, 0, 0};
    double media = 0;

    for (int i = 0; i < 3; i++) {
        cout << "Digite a nota " << i + 1 << ": ";
        cin >> notas[i];
        media += notas[i];
    }
    media /= 3;
    cout << "Media das notas: " << media << endl;

    if (media >= 5) {
        cout << "Estudante aprovasdo! :)" << endl;
    }
    else {
        cout << "Estudante reprovado! :(" << endl;
    }
}