{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOhoDuuZzYm+5muvc0wcJ6Q"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 60,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kUy7MnC1Xf3P",
        "outputId": "69cec8b1-28db-487f-c8c4-23611943a50e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hola\n",
            "Hola\n",
            "Que haces?\n",
            "The current time is 04:42 AM\n",
            "Puto\n",
            "Hola\n",
            "Que haces?\n",
            "The current time is 04:43 AM\n",
            "Nada y tu?\n",
            "The current time is 04:43 AM\n",
            "Nada y tu?\n",
            "The current time is 04:43 AM\n",
            "Hola\n",
            "Hola\n",
            "Puto\n",
            "Puto\n",
            "Que haces?\n",
            "The current time is 04:43 AM\n",
            "Hello\n",
            "Nada y tu?\n",
            "Nada\n",
            "The current time is 04:44 AM\n",
            "Hola\n",
            "Nada\n",
            "Hola\n",
            "Que haces?\n",
            "Nada y tu?\n",
            "The current time is 04:44 AM\n",
            "Aqui jugando\n",
            "The current time is 04:43 AM\n",
            "Hola\n",
            "Nada y tu?\n",
            "Como estas?\n",
            "The current time is 04:44 AM\n",
            "Hola\n",
            "Hola\n",
            "Que haces?\n",
            "The current time is 04:44 AM\n",
            "Que haces?\n",
            "The current time is 04:44 AM\n",
            "Hla\n",
            "Como estas?\n",
            "bien y tu?\n",
            "The current time is 04:45 AM\n",
            "Tambien bien\n",
            "The current time is 04:45 AM\n",
            "Que bueno\n",
            "The current time is 04:45 AM\n",
            "Hola\n",
            "Que bueno\n",
            "Que haces?\n",
            "The current time is 04:45 AM\n",
            "Nada y tu?\n",
            "The current time is 04:45 AM\n",
            "Puto\n",
            "Como estas?\n",
            "Bien y tu?\n",
            "The current time is 04:45 AM\n",
            "Como estas?\n",
            "The current time is 04:45 AM\n",
            "what time is it?\n",
            "The current time is 04:50 AM\n"
          ]
        }
      ],
      "source": [
        "from chatterbot import ChatBot\n",
        "import logging\n",
        "\n",
        "logging.basicConfig(level=logging.INFO)\n",
        "\n",
        "\n",
        "bot = ChatBot(\n",
        "    \n",
        "    'Base de datos_Calculadora_Noe',\n",
        "    storage_adapter='chatterbot.storage.SQLStorageAdapter',\n",
        "    database_uri=None,\n",
        "    logic_adapters=[\n",
        "        'chatterbot.logic.BestMatch',\n",
        "        'chatterbot.logic.MathematicalEvaluation',\n",
        "        'chatterbot.logic.TimeLogicAdapter'\n",
        "        \n",
        "        \n",
        "    ]\n",
        ")\n",
        "while True:\n",
        "  try:\n",
        "    bot_input = bot.get_response(input())\n",
        "    print(bot_input)\n",
        "\n",
        "  except(KeyboardInterrupt, EOFError, SystemExit):\n",
        "    break\n",
        "\n",
        "\n",
        "# OPCIONES PARA PREGUNTAR:\n",
        "\n",
        "#  What time is it?\n",
        "#  7 * 7\n",
        "#  6 + 6\n",
        "#  5 - 2\n",
        "# What is 7 plus 7?\n",
        "      #etc etc etc"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install chatterbot2"
      ],
      "metadata": {
        "id": "Vgc6wi7cXg-R"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}