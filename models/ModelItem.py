from flask import Flask, render_template, url_for, redirect, flash, session, request, jsonify
from conexao_mysql import *
from models.Form import *
 

def ItemRegister():
    form = ModelFormItem()
    if request.method == 'POST':
        grupo = form.grupo.data.upper()
        subgrupo = form.subgrupo.data.upper()
        nome = form.nome.data.upper()
        descricao = form.descricao.data.upper()
        un = form.un.data.upper()
        tipo = form.tipo.data.upper()
        codigointerno = form.codigointerno.data.upper()
        ean = form.ean.data
        dun = form.dun.data

        cor = form.cor.data.upper()
        tamanho = form.tamanho.data.upper()
        largura = form.largura.data
        altura = form.altura.data
        comprimento = form.comprimento.data
        pesoliquido = form.pesoliquido.data
        pesobruto = form.pesobruto.data
        estoqueminino = form.estoqueminino.data
        estoquemaximo = form.estoquemaximo.data
        leadtime = form.leadtime.data

        loteminino = form.loteminino.data
        lotemaximo = form.lotemaximo.data
        ncm = form.ncm.data
        cest = form.cest.data
        classificacao = form.classificacao.data.upper()
        ativo = form.ativo.data.upper()
        id_company = form.id_company.data

        try:
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM items WHERE nome = %s', [nome])
            cursor.fetchone()
            cursor.close()
            count = cursor.rowcount
            if count == 0:
                cursor = mysql.connection.cursor()
                cursor.execute('''INSERT INTO items 
                (grupo, subgrupo, nome, descricao, un, tipo, codigointerno, ean, dun, 
                cor, tamanho, largura, altura, comprimento, 
                pesoliquido, pesobruto, estoqueminino, estoquemaximo, leadtime, 
                loteminino, lotemaximo, ncm, cest, classificacao, ativo,
                id_company) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s)''',
                [grupo, subgrupo, nome, descricao, un, tipo, codigointerno, ean, dun, 
                cor, tamanho, largura, altura, comprimento, 
                pesoliquido, pesobruto, estoqueminino, estoquemaximo, leadtime, 
                loteminino, lotemaximo, ncm, cest, classificacao, ativo,
                id_company])
                mysql.connection.commit()
                flash('Item Created Successfully...!!!', 'success')
            else:
                flash('Item Found...!!!', 'danger')
        except Exception as error:
            print(error)


def ItemUpdate():
    form = ModelFormItem()
    if request.method == 'POST':
        grupo = form.grupo.data.upper()
        subgrupo = form.subgrupo.data.upper()
        nome = form.nome.data.upper()
        descricao = form.descricao.data.upper()
        un = form.un.data.upper()
        tipo = form.tipo.data.upper()
        codigointerno = form.codigointerno.data.upper()
        ean = form.ean.data
        dun = form.dun.data

        cor = form.cor.data.upper()
        tamanho = form.tamanho.data.upper()
        largura = form.largura.data
        altura = form.altura.data
        comprimento = form.comprimento.data
        pesoliquido = form.pesoliquido.data
        pesobruto = form.pesobruto.data
        estoqueminino = form.estoqueminino.data
        estoquemaximo = form.estoquemaximo.data
        leadtime = form.leadtime.data

        loteminino = form.loteminino.data
        lotemaximo = form.lotemaximo.data
        ncm = form.ncm.data
        cest = form.cest.data
        classificacao = form.classificacao.data.upper()
        ativo = form.ativo.data.upper()
        id = form.id.data
        id_company = form.id_company.data

        cursor = mysql.connection.cursor()
        cursor.execute('''UPDATE items 
        SET grupo = %s, subgrupo = %s, nome = %s, descricao = %s, un = %s, 
        tipo = %s, codigointerno = %s, ean = %s, dun = %s, 
        cor = %s, tamanho = %s, largura = %s, altura = %s, comprimento = %s, 
        pesoliquido = %s, pesobruto = %s, estoqueminino = %s, estoquemaximo = %s, leadtime = %s, 
        loteminino = %s, lotemaximo = %s, ncm = %s, cest = %s,
        classificacao = %s, ativo = %s, id_company = %s
        WHERE id = %s''',
        [grupo, subgrupo, nome, descricao, un, tipo, codigointerno, ean, dun, 
        cor, tamanho, largura, altura, comprimento, pesoliquido, pesobruto, 
        estoqueminino, estoquemaximo, leadtime, loteminino, lotemaximo, ncm, cest, 
        classificacao, ativo, id_company, id])
        mysql.connection.commit()
        flash("Item Updated Successfully...!!!", "success")