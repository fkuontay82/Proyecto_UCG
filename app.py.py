PAGES = {
    "Modulo 1: Carga de información": "modulo1",
    "Modulo 2: Registro de: interes, monto, cuotas": "modulo2",
    "Modulo 3: Nada": "modulo3"
}
selection = st.sidebar.radio("Navegación", list(PAGES.keys()))
page_id = PAGES[selection]

if page_id == "modulo1":
    st.header("Modulo 1: Carga de información")
    uploaded_files = st.file_uploader(
        "Upload data", accept_multiple_files=True, type="csv"
    )
    for uploaded_file in uploaded_files:
        df = pd.read_csv(uploaded_file)
        st.write(df)
elif page_id == "modulo2":
    st.header("Modulo 2: Registro de: interes, monto, cuotas")
    monto = st.number_input ("Ingrese el monto:", min_value = 0, max_value = 10000, value = 1000)
    interes = st.number_input("Ingrese el interes:",min_value = 0.0 , max_value = 1.0, value=0.10)
    anios = st.number_input ("Ingrese el numero de años del prestamo:", value = 1)
    numero_pagos = st.number_input ("Ingrese el numero de pagos anuales:", value = 12)

    cuota = lf.cuota_prestamo(monto, interes,anios,numero_pagos)
    st.write("su cuota mensual es:",cuota)
elif page_id == "modulo3":
    st.header("Modulo 3: Nada")
    st.write("Este módulo está vacío por ahora.")

else:
    st.write("Se encuentra en el módulo 3")
