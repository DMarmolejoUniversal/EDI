
EDI  = "UNB+UNOA:1+094200005560139700:30:009840+UNIVERSAL:30:1633292+260902:0922+75'UNH+7500001+DELJIT:D:04B:UN:GMI061'BGM+307::6:S1+202609020005'DTM+137:202609020721:203'NAD+BY+9840::92'NAD+SF+1633292::92'NAD+ST+9840::92'SEQ+40+3631001'DTM+194:202609180901:203'GIR+4+PV727547:VV'LIN+++23805133:IN'IMD+++:::VALVE'RFF+ON:NIL'LOC+11+UN-WT::92'LOC+159+UN-WT D9840::92'QTY+113:10'SEQ+40+3631002'DTM+194:202610070632:203'GIR+4+PV727547:VV'LIN+++23091380:IN'IMD+++:::3/0'RFF+ON:NIL'LOC+11+UN-WT::92'LOC+159+UN-WT X0654Y0710::92'QTY+113:1'LIN+++23091380:IN'IMD+++:::5/0'RFF+ON:NIL'LOC+11+UN-WT::92'LOC+159+UN-WT X0654Y0710::92'QTY+113:4'LIN+++24114724:IN'IMD+++:::3/0'RFF+ON:NIL'LOC+11+UN-WT::92'LOC+159+UN-WT X0654Y0710::92'QTY+113:1'LIN+++23615827:IN'IMD+++:::SENSOR'RFF+ON:NIL'LOC+11+UN-WT::92'LOC+159+UN-WT X0654Y0710::92'QTY+113:5'LIN+++23764410:IN'IMD+++:::5/0'RFF+ON:NIL'LOC+11+UN-WT::92'LOC+159+UN-WT X0654Y0710::92'QTY+113:4'SEQ+40+3631003'DTM+194:202610070632:203'GIR+4+PV727547:VV'LIN+++23091380:IN'IMD+++:::3/0'RFF+ON:NIL'LOC+11+UN-WT::92'LOC+159+UN-WT X0654Y0702::92'QTY+113:1'LIN+++23091380:IN'IMD+++:::5/0'RFF+ON:NIL'LOC+11+UN-WT::92'LOC+159+UN-WT X0654Y0702::92'QTY+113:4'LIN+++24114724:IN'IMD+++:::3/0'RFF+ON:NIL'LOC+11+UN-WT::92'LOC+159+UN-WT X0654Y0702::92'QTY+113:1'LIN+++23615827:IN'IMD+++:::SENSOR'RFF+ON:NIL'LOC+11+UN-WT::92'LOC+159+UN-WT X0654Y0702::92'QTY+113:5'LIN+++23764410:IN'IMD+++:::5/0'RFF+ON:NIL'LOC+11+UN-WT::92'LOC+159+UN-WT X0654Y0702::92'QTY+113:4'SEQ+40+3631004'DTM+194:202610070647:203'GIR+4+PM105388:VV'LIN+++24976744:IN'IMD+++:::TIRE'RFF+ON:NIL'LOC+11+UN-WT::92'LOC+159+UN-WT X0654Y0710::92'QTY+113:8'LIN+++24247436:IN'IMD+++:::DISC WHEEL'RFF+ON:NIL'LOC+11+UN-WT::92'LOC+159+UN-WT X0654Y0710::92'QTY+113:9'LIN+++22846912:IN'IMD+++:::TIRE'RFF+ON:NIL'LOC+11+UN-WT::92'LOC+159+UN-WT X0654Y0710::92'QTY+113:1'SEQ+40+3631005'DTM+194:202610070647:203'GIR+4+PM105388:VV'LIN+++22846912:IN'IMD+++:::TIRE'RFF+ON:NIL'LOC+11+UN-WT::92'LOC+159+UN-WT X0654Y0702::92'QTY+113:1'LIN+++24247436:IN'IMD+++:::DISC WHEEL'RFF+ON:NIL'LOC+11+UN-WT::92'LOC+159+UN-WT X0654Y0702::92'QTY+113:1'UNT+118+7500001'UNZ+1+75'"
def Leer_EDI(edi):
    resultado = {
        "General": {},
        "Detalle": []
    }
    seq = None
    fecha_seq = None
    hora_seq = None
    gir = None
    posicion = None
    ubicacion = None
    parte = None
    descripcion = None
    segmentos = edi.split("'")
    for segmento in segmentos:
        segmento = segmento.strip()
        if not segmento:
            continue
        campos = segmento.split("+")
        tipo = campos[0]
        if tipo == "UNB":
            resultado["General"]["Tipo_Intercambio"] = "UNB"
            if len(campos) > 1:
                resultado["General"]["Sintaxis"] = campos[1]
            if len(campos) > 2:
                datos = campos[2].split(":")
                if len(datos) > 0:
                    resultado["General"]["Emisor"] = datos[0]
            if len(campos) > 3:
                datos = campos[3].split(":")
                if len(datos) > 0:
                    resultado["General"]["Receptor"] = datos[0]
            if len(campos) > 4:
                datos = campos[4].split(":")
                if len(datos) >= 2:
                    resultado["General"]["Fecha_Intercambio"] = datos[0]
                    resultado["General"]["Hora_Intercambio"] = datos[1]
        elif tipo == "UNH":
            if len(campos) > 1:
                resultado["General"]["Mensaje_ID"] = campos[1]
            if len(campos) > 2:
                datos = campos[2].split(":")
                if len(datos) > 0:
                    resultado["General"]["Tipo_Mensaje"] = datos[0]
                if len(datos) > 1:
                    resultado["General"]["Version"] = datos[1]
        elif tipo == "BGM":
            if len(campos) > 1:
                datos = campos[1].split(":")
                if len(datos) > 0:
                    resultado["General"]["Tipo_Documento"] = datos[0]
            if len(campos) > 2:
                resultado["General"]["Documento"] = campos[2]
        elif tipo == "DTM":
            if len(campos) > 1:
                datos = campos[1].split(":")
                if len(datos) >= 2:
                    tipo_fecha = datos[0]
                    valor = datos[1]
                    if tipo_fecha == "137":
                        resultado["General"]["Fecha_Documento"] = valor
                    elif tipo_fecha == "194":
                        fecha_seq = valor[:8]
                        hora_seq = valor[8:12]
        elif tipo == "NAD":
            if len(campos) > 2:
                tipo_nad = campos[1]
                valor = campos[2].split(":")[0]
                if tipo_nad == "BY":
                    resultado["General"]["Buyer"] = valor
                elif tipo_nad == "SF":
                    resultado["General"]["Ship_From"] = valor
                elif tipo_nad == "ST":
                    resultado["General"]["Ship_To"] = valor
        elif tipo == "SEQ":
            if len(campos) > 2:
                seq = campos[2]
        elif tipo == "GIR":
            if len(campos) > 2:
                gir = campos[2].split(":")[0]
        elif tipo == "LIN":
            parte = None
            descripcion = None
            posicion = None
            ubicacion = None
            if len(campos) > 3:
                parte = campos[3].split(":")[0]
        elif tipo == "IMD":
            if len(campos) > 3:
                datos = campos[3].split(":")
                if len(datos) > 0:
                    descripcion = datos[-1]
        elif tipo == "LOC":
            if len(campos) > 2:
                tipo_loc = campos[1]
                valor = campos[2].split("::")[0]
                if tipo_loc == "159":
                    ubicacion = valor
                    if " " in valor:
                        posicion = valor.split(" ")[-1]
                    else:
                        posicion = valor
        elif tipo == "QTY":
            if len(campos) > 1:
                datos = campos[1].split(":")
                if len(datos) >= 2:
                    if datos[0] == "113":
                        cantidad = datos[1]
                        try:
                            cantidad = float(cantidad)
                            if cantidad.is_integer():
                                cantidad = int(cantidad)
                        except:
                            pass
                        resultado["Detalle"].append({
                            "SEQ": seq,
                            "Fecha": fecha_seq,
                            "Hora": hora_seq,
                            "GIR": gir,
                            "Parte": parte,
                            "Descripcion": descripcion,
                            "Cantidad": cantidad,
                            "Ubicacion": ubicacion,
                            "Posicion": posicion
                        })
    return resultado
resultado = Leer_EDI(EDI)
for k in resultado["General"].keys():
    print(str(k)+":"+str(resultado["General"][k]))
for D in resultado["Detalle"]:
    print(D)
