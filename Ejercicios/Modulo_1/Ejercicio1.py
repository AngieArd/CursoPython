using System;

class Program {
    static void Main(string[] args) {
        int[,] matrix = new int[4, 4];
        int[] instructions = {1, 2, -1, 1, 0, 1, 2, -1, -1, -2};
        int x = 0;
        int y = 0;

        // Inicializar la matriz con O's
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                matrix[i, j] = 'O';
            }
        }

        // Mover la X según las instrucciones
        for (int i = 0; i < instructions.Length; i += 2) {
            int dx = instructions[i];
            int dy = instructions[i + 1];

            // Verificar si la X se sale de la matriz
            if (x + dx < 0) {
                dx = -x;
            } else if (x + dx > 3) {
                dx = 3 - x;
            }
            if (y + dy < 0) {
                dy = -y;
            } else if (y + dy > 3) {
                dy = 3 - y;
            }

            // Mover la X
            x += dx;
            y += dy;
        }

        // Imprimir la matriz final
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (i == y && j == x) {
                    Console.Write('X');
                } else {
                    Console.Write((char)matrix[i, j]);
                }
            }
            Console.WriteLine();
        }
    }
}

