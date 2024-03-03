import PySimpleGUI as sg

table_data = []
layout_exponential_graph = [
    [
        sg.Text(
            "Exponential Equation (y = a(k)ˣ)",
            expand_x=True,
            font="Georgia 20",
            justification="center",
            pad=(20, 20),
        )
    ],
    [
        sg.Column(
            [
                [
                    sg.Text("a = ", pad=(20, 0)),
                    sg.Input(key="-INPUT_A_EXPONENTIAL-", size=(5, 1))
                ],
                [
                    sg.Text("k = ", pad=(20, 0)),
                    sg.Input(key="-INPUT_K_EXPONENTIAL-", size=(5, 1))
                ],
                [
                    sg.Text("First x value = ", pad=(20, 0)),
                    sg.Input(key="-INPUT_X_START_EXPONENTIAL-", size=(5, 1))
                ],
                [
                    sg.Text("Last x value = ", pad=(20, 0)),
                    sg.Input(key="-INPUT_X_END_EXPONENTIAL-", size=(5, 1))
                ],
                [
                    sg.Button(
                        "Generate Table",
                        key="-CREATE_TABLE_EXPONENTIAL-",
                        pad=(20, 10),
                        size=(15, 1)
                    ),
                    sg.Button(
                        "Clear",
                        key="-CLEAR_TABLE_EXPONENTIAL-",
                        pad=(20, 10),
                        size=(10, 1)
                    ),
                ],
                [
                    sg.Table(
                        key="-TABLE_EXPONENTIAL-",
                        headings=["X", "Y"],
                        values=table_data,
                        justification="center",
                        expand_x=True,
                        background_color="black",
                        text_color="white",
                        pad=(20, 10),
                        size=(40, 20)
                    )
                ]
            ],
        ),
        sg.VSeparator(),
        sg.Column(
            [
                [
                    sg.Button(
                        "Generate Graph",
                        key="-CREATE_GRAPH_EXPONENTIAL-",
                        pad=(20, 5)
                    ),
                    sg.Button(
                        "Clear Graph",
                        key="-CLEAR_GRAPH_EXPONENTIAL-",
                        pad=(20, 5)
                    )
                ],
                [sg.Canvas(key="-GRAPH_EXPONENTIAL-", pad=(20, 5))]
            ]
        )
    ]
]
