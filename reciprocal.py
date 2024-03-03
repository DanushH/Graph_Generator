import PySimpleGUI as sg

table_data = []
layout_reciprocal_graph = [
    [
        sg.Text(
            "Reciprocal Equation (y = a / x)",
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
                    sg.Input(key="-INPUT_A_RECIPROCAL-", size=(5, 1))
                ],
                [
                    sg.Text("First x value = ", pad=(20, 0)),
                    sg.Input(key="-INPUT_X_START_RECIPROCAL-", size=(5, 1))
                ],
                [
                    sg.Text("Last x value = ", pad=(20, 0)),
                    sg.Input(key="-INPUT_X_END_RECIPROCAL-", size=(5, 1))
                ],
                [
                    sg.Button(
                        "Generate Table",
                        key="-CREATE_TABLE_RECIPROCAL-",
                        pad=(20, 10),
                        size=(15, 1)
                    ),
                    sg.Button(
                        "Clear",
                        key="-CLEAR_TABLE_RECIPROCAL-",
                        pad=(20, 10),
                        size=(10, 1)
                    ),
                ],
                [
                    sg.Table(
                        key="-TABLE_RECIPROCAL-",
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
                        key="-CREATE_GRAPH_RECIPROCAL-",
                        pad=(20, 5)
                    ),
                    sg.Button(
                        "Clear Graph",
                        key="-CLEAR_GRAPH_RECIPROCAL-",
                        pad=(20, 5)
                    )
                ],
                [sg.Canvas(key="-GRAPH_RECIPROCAL-", pad=(20, 5))]
            ]
        )
    ]
]
