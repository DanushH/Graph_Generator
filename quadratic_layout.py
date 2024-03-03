import PySimpleGUI as sg

table_data = []
layout_quadratic_graph = [
    [
        sg.Text(
            "Quadratic Equation (y = ax² +bx + c)",
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
                    sg.Input(key="-INPUT_A_QUADRATIC-", size=(5, 1))
                ],
                [
                    sg.Text("b = ", pad=(20, 0)),
                    sg.Input(key="-INPUT_B_QUADRATIC-", size=(5, 1))
                ],
                [
                    sg.Text("c = ", pad=(20, 0)),
                    sg.Input(key="-INPUT_C_QUADRATIC-", size=(5, 1))
                ],
                [
                    sg.Text("First x value = ", pad=(20, 0)),
                    sg.Input(key="-INPUT_X_START_QUADRATIC-", size=(5, 1))
                ],
                [
                    sg.Text("Last x value = ", pad=(20, 0)),
                    sg.Input(key="-INPUT_X_END_QUADRATIC-", size=(5, 1))
                ],
                [
                    sg.Button(
                        "Generate Table",
                        key="-CREATE_TABLE_QUADRATIC-",
                        pad=(20, 10),
                        size=(15, 1)
                    ),
                    sg.Button(
                        "Clear",
                        key="-CLEAR_TABLE_QUADRATIC-",
                        pad=(20, 10),
                        size=(10, 1)
                    ),
                ],
                [
                    sg.Table(
                        key="-TABLE_QUADRATIC-",
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
                        key="-CREATE_GRAPH_QUADRATIC-",
                        pad=(20, 5)
                    ),
                    sg.Button(
                        "Clear Graph",
                        key="-CLEAR_GRAPH_QUADRATIC-",
                        pad=(20, 5)
                    )
                ],
                [sg.Canvas(key="-GRAPH_QUADRATIC-", pad=(20, 5))]
            ]
        )
    ]
]
