#!/usr/bin/env bash

zenity --question --title='Salvar Arquivo' --width='250'  --text='Deseja salvar ?'

resposta=$?

# Variável resposta armazena 0 ou 1

if [ $resposta -eq 0 ] 
then
  
fi

# Legendas:
#
# 0 -> OK
# 1 -> CANCEL
