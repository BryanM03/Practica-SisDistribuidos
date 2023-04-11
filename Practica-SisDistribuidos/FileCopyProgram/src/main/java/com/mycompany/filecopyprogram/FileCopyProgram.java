/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */
package com.mycompany.filecopyprogram;

import java.io.*;
import java.util.Scanner;

public class FileCopyProgram {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // Pedir al usuario la ruta del archivo a copiar
        System.out.print("Ingrese la ruta del archivo a copiar: ");
        String rutaArchivo = scanner.nextLine();

        // Pedir al usuario el nombre del archivo destino
        System.out.print("Ingrese el nombre del archivo destino: ");
        String nombreArchivoDestino = scanner.nextLine();

        // Variable compartida para almacenar el contenido del archivo original
        StringBuilder contenidoArchivo = new StringBuilder();

        // Crear el hilo para la lectura de entrada desde el archivo
        Thread hiloEntrada = new Thread(new Runnable() {
            public void run() {
                try {
                    FileInputStream entrada = new FileInputStream(rutaArchivo);
                    BufferedInputStream entradaBuffer = new BufferedInputStream(entrada);
                    int b;
                    while ((b = entradaBuffer.read()) != -1) {
                        synchronized (contenidoArchivo) {
                            contenidoArchivo.append((char) b);
                        }
                        synchronized (System.out) {
                            System.out.write(b);
                        }
                    }
                    // Cerrar el stream de entrada
                    entradaBuffer.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        });

        // Crear el hilo para la escritura de salida al archivo destino
        Thread hiloSalida = new Thread(new Runnable() {
            public void run() {
                try {
                    FileOutputStream salida = new FileOutputStream(nombreArchivoDestino);
                    BufferedOutputStream salidaBuffer = new BufferedOutputStream(salida);
                    boolean hecho = false;
                    while (!hecho) {
                        int b = System.in.read();
                        if ((char) b == '#') {
                            hecho = true;
                        } else {
                            salidaBuffer.write(b);
                        }
                    }
                    // Agregar el contenido original al nuevo contenido
                    synchronized (contenidoArchivo) {
                        byte[] nuevoContenido = (contenidoArchivo.toString() + System.lineSeparator()).getBytes();
                        salidaBuffer.write(nuevoContenido);
                    }
                    // Cerrar el stream de salida
                    salidaBuffer.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        });

        // Iniciar los hilos de entrada y salida
        hiloEntrada.start();
        hiloSalida.start();
    }
}
