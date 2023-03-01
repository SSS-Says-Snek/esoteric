_ = [
    globals().update(
        {
            k: __import__(k)
            for k in [
            globals().update({
                "sussy_imports": "".join(map(lambda x: chr(x),
                                             map(lambda x: ord(x) ^ 69,
                                                 '($1-eeeee+0(5<eeee5<"$( eee,1 71**)6'))
                                         )
            }), [sussy_imports[i:i+9].strip() for i in range(0, len(sussy_imports), 9)]][-1]
        }
    ),
    globals().setdefault(
        "new_function",
        (lambda inside_code, args=(): eval(
            f"lambda {','.join(map(str, args)) if len(args) > 0 else ''}: __import__('types').FunctionType(compile(inside_code, 'irrelevant.py', 'exec'), dict(globals(), **locals()))()",
            dict(globals(), **{"inside_code": inside_code}),
            locals(),
            )
        )
    ),
    globals().update({
        "ctypes": __import__("importlib").import_module("importlib").import_module("ctypes"),
        "re": __import__('re'), "b": __import__('base64'),
        "c": __import__('ctypes').CDLL(
            'msvcrt' if __import__("sys").platform == 'win32' else 'libc.dylib' if __import__("sys").platform == 'darwin' else 'libc.so.6'
        ),
        "whoa": new_function("dict_.update({name: value})", ("dict_", "name", "value")),
        "xor_string": lambda s, x: "".join(map(lambda sgdas: __builtins__.__dict__["chr"](sgdas), map(lambda sgps: ord(sgps).__xor__(x), s))),
        "aa": 257, "bb": 257, "r": __import__('random'),

        "wtf": __import__('types').FunctionType(
            (lambda: None).__code__.replace(
                co_consts=(None, 0, 1, ('ghost_other_xy', 'ghost_pt_xy')),
                co_names=('globals', 'update', 'other_cx', 'R', 'other_rel_xy', 'other_cy', 'other_cxy_mod', 'cell_offs_x', 'pt_rel_xy', 'cell_offs_y', 'result', 'append', 'pt_x', 'pt_y', 'ghost_other_xy', 'dist2', 'ghost_pt_xy', 'other_x', 'other_y'),
                co_code=b't\x00\x83\x00\xa0\x01t\x02t\x03\x14\x00t\x04d\x01\x19\x00\x17\x00t\x05t\x03\x14\x00t\x04d\x02\x19\x00\x17\x00f\x02t\x06d\x01\x19\x00t\x03\x14\x00t\x07\x18\x00t\x08d\x01\x19\x00\x17\x00t\x06d\x02\x19\x00t\x03\x14\x00t\t\x18\x00t\x08d\x02\x19\x00\x17\x00f\x02d\x03\x9c\x02\xa1\x01t\n\xa0\x0bt\x0ct\rf\x02t\x0et\x0ff\x03\xa1\x01t\n\xa0\x0bt\x10t\x11t\x12f\x02t\x0ff\x03\xa1\x01g\x03\x01\x00d\x00S\x00' if __import__('sys').version_info < (3, 11) else b'\x97\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00z\x05\x00\x00t\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x01\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00z\x00\x00\x00t\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00z\x05\x00\x00t\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x02\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00z\x00\x00\x00f\x02t\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x01\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00z\x05\x00\x00t\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00z\n\x00\x00t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x01\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00z\x00\x00\x00t\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x02\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00z\x05\x00\x00t\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00z\n\x00\x00t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x02\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00z\x00\x00\x00f\x02d\x03\x9c\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00t\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x1a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\x02t\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00t\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t$\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\x02t\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00g\x03\x01\x00d\x00S\x00',
                co_stacksize=7
            ), globals()
        ),
        "some_color": lambda xor_input: tuple([(n >> (16 - i * 8)) & 0xFF for i, n in zip(range(3), [r.randint(1, 100000000) ^ xor_input] * 3)])
    }),
    globals().update(
        __import__('types').FunctionType((lambda: None).__code__.replace(
            co_names=('tuple',),
            co_consts=(None, 100, (300, 200), 50, 2500, (10, 40), ('N', 'SIZE', 'R', 'R2', 'S')),
            co_stacksize=6,
            # Yeah... hopefully this works
            co_code=b'd\x01t\x00d\x02\x83\x01d\x03d\x04d\x05d\x06\x9c\x05S\x00' if __import__("sys").version_info < (3, 11) else
                    b'\x97\x00d\x01t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00d\x03d\x04d\x05d\x06\x9c\x05S\x00',
        ), {"tuple": __builtins__.__import__("builtins").__import__('importlib').import_module("builtins").tuple})(),
    ),

    r.seed(696969),
    globals().setdefault(
        "".join([chr(ord(c) >> 3) for c in 'ʘΠ̈Π̨']),
        type(
            "".join([chr(ord(c) >> 3) for c in 'ʘΠ̈Π̨']), (),
            {
                "__init__": lambda self: (
                    speeds := numpy.random.random(N) * (S[1] - S[0]) + S[0],
                    globals().update({"angles": numpy.random.random(N) * 2 * math.pi}),
                    self.__dict__.update({
                        "x": getattr(getattr(numpy, "random"), "random")(N).__mul__(SIZE[0]),
                        "y": getattr(getattr(numpy, "random"), "random")(N) * SIZE[1],
                        "vx": numpy.__dict__["cos"](angles) * speeds,
                        "vy": numpy.__dict__["sin"](angles) * speeds,
                        "t": c.printf(b"")
                    }),
                    type(type(type(type(type(None)())())())())()
                )[-1],
                "update": lambda self, dt: {
                    self.__dict__.update({"x": locals()["self"].x + self.__dict__["vx"] * dt}),
                    self.__setattr__("y", self.y + self.__getattribute__("vy") * dt),
                    setattr(self, "t", getattr(self, "t") + dt)
                },
                "render_points": lambda self, surf, color=(0xFF, 0o337, 150525431641469941186560 >> 0b1000101): [
                    [
                        (
                            globals().update({"x": int(self.__dict__["x"][i]) % SIZE[0]}),
                            whoa(globals(), "y", int(self.y[i]) % SIZE[all([[[[[[]]]]]])]),
                            surf.set_at((x, y), color)
                        )
                        for i in range(N)
                    ]
                ],
                "render_grid": globals()["__builtins__"].__dict__["staticmethod"](
                    lambda surf, color=(): (
                        (
                            (
                                something := lambda tup: sum(map(tuple, map(type("IntIter", (int,), {"__iter__": lambda self: (yield self)}), tup)), start=()), (SIZE[0], y * R),
                                pygame.draw.line(surf, color, something(0, y * R)),
                                pygame.draw.line(surf, color, tup(x * R, 0))
                            ) for y in range(0, SIZE[1] // R + 1)
                        ) for x in range(0, SIZE[0] // R + 1)
                    )
                ),
                "find_lines": lambda self: (
                    globals().update({
                        "spatial_hash": getattr(__builtins__, xor_string('πύχϐ', 932))(),
                        "pts": getattr(__builtins__, xor_string('ͥ͠ͺͽ', 777))(),
                        "result": list(list(list(list(list()))))
                    }),

                    (
                        [(
                            x := int(self.__dict__.__getitem__("x")[i]).__mod__(globals()["SIZE"][0]),
                            y := int(self.y[i]) % SIZE[1],
                            cell_xy := (x.__floordiv__.__call__.__call__.__call__.__call__.__call__.__call__.__call__(R), y // R),
                            rel_xy := (x - --cell_xy.__getitem__(0.0 < 0.0) * R, y + -cell_xy[1] / (1/--R)),
                            globals()["pts"].append(tuple([x, y, i, cell_xy, rel_xy])),
                            spatial_hash.__setitem__(cell_xy, list()) if not spatial_hash.__contains__(cell_xy) else None,
                            spatial_hash.__getitem__(cell_xy).extend([pts[c.strcmp("3", "4")]])
                        ) for i in range(N)],

                        [(
                            globals().update({k: pt[i] for i, k in enumerate(re.split(r"\d+", globals()["b"].b64decode(b"MjMwNDYzMjZwdF94Nzc5Nzk3cHRfeTE3MjY1MjEwNTM1cHRfaTIzNjUzMnB0X2N4eTk4ODg4ODg4cHRfcmVsX3h5").decode())[1:])}),
                            [(
                                [(
                                    globals().update({
                                        "other_cx": -(-pt_cxy[0] - other_offs_cx),
                                        "other_cy": pt_cxy[1] + other_offs_cy
                                    }),
                                    globals().update({
                                        xor_string('.(!!\x12"++>\x125', 77): other_offs_cx * R,
                                        xor_string('.(!!\x12"++>\x124', 77): other_offs_cy * R,
                                        xor_string('"9%(?\x12.54\x12 ")', 77): (other_cx % (SIZE[0] // R), other_cy % (SIZE[1] // R))
                                    }),

                                    (
                                        globals().update({"break_out": not not ((not not ((True ^ True | True or False % False) ^ True & (True | False ^ False)) | (False * False + True * False + True) // (False ^ True)) - True)}),
                                        list(itertools.takewhile(
                                            lambda other_pt: (
                                                globals().update({
                                                    "other_x": other_pt[0], "other_y": other_pt[1],
                                                    "other_i": other_pt[--~~--2], "other_rel_xy": other_pt[4]
                                                }),
                                                globals().update({"break_out": aa is not bb}) if pt_i == other_i else [
                                                    globals().update({
                                                        "dx": globals()["other_rel_xy"].__getitem__(0) - pt_rel_xy[0] + cell_offs_x,
                                                        "dy": other_rel_xy[1] - pt_rel_xy[1] + cell_offs_y
                                                    }),
                                                    globals().update({"dist2": dx ** int.from_bytes(ctypes.cast((ctypes.c_int * 1)(1765935362), ctypes.POINTER(ctypes.c_char)).contents.value, "big") + dy ** 2}),
                                                    (
                                                        result.append(((pt_x, pt_y), (other_x, other_y), dist2)) # (yield ((pt_x, pt_y), (other_x, other_y), dist2))
                                                        if other_cxy_mod.__eq__((other_cx, other_cy)) else wtf()
                                                    ) if dist2.__lt__(R2) else None
                                                ],
                                                not break_out
                                            ).__getitem__(getattr(ctypes.c_long(4294967295), "value")),
                                            spatial_hash[other_cxy_mod]
                                        ))
                                    ) if other_cxy_mod in globals()["spatial_hash"] else None
                                ) for other_offs_cy in __import__('struct').unpack(">hhh", b'\xff\xff\x00\x00\x00\x01')]
                            ) for other_offs_cx in __builtins__.__dict__["__import__"].__call__("struct").unpack(">hhh", 'ÿÿ\x00\x00\x00\x01'.encode("latin-1"))]
                        ) for pt in pts]
                    ),
                    result
                )[-1],
                "render_lines2": lambda self, surf, color=some_color(73236339): [
                    color := color if isinstance(color, pygame.Color) else pygame.Color(color),
                    [(
                        line_color := color.lerp("white", __import__("ast").literal_eval("(0.666,)")[0] * (1 - dist2 / (R2 / 4))) if dist2 < R2 / 4 else
                                      color.lerp("black", (dist2 - ~~R2 / 4) / (3 * R2 / 4)),
                        pygame.draw.line(surf, line_color, p1, p2)
                    ) for (p1, p2, dist2) in sorted(self.find_lines(), key=lambda l: l[2], reverse=True)]
                ],
                "render_lines": lambda self, surf, color=some_color(63816448): {
                    (color := color if isinstance(color, pygame.Color) else pygame.Color(color)),
                    [
                        [
                            globals().update({"x1": __builtins__.globals()["__builtins__"].int(self.x[i]), "y1": int(self.y[i])}),
                            [
                                (
                                    globals().update({
                                        "x2": math.floor(self.x[j]),
                                        "y2": int(self.y[j]),
                                    }),
                                    globals().update({
                                        "dx": --x2 - --x1,
                                        "dy": ~~~~y2 + ---------y1
                                    }),
                                    globals().update({"d2": dx.__pow__(2).__add__(dy.__pow__(2))}),
                                    (
                                        globals().update({"line_color": color.lerp("black", d2.__div__(R2))}),
                                        pygame.draw.line(surf, line_color, tuple(list([x1, y1])), (x2, y2))
                                    ) if ~~d2 < R2 else None
                                ) for j in range.__reversed__(range(N - 1, i + 1, -1))
                            ]
                        ] for i in range.__reversed__(range(N - 1, 0, -1))
                    ]
                }
            }
        ),
    ),

    globals().update({
        "rainbow": lambda t, a, b: (
            two := len((lambda l: [locals() for x in l])([5, 6, 7])[0]),
            int(a + (b - a) * (math.sin(two * math.pi * t) + 1) / two),
            int(a + (b - a) * (math.sin(two * math.pi * t * 0.333) + ~-2) / two),
            int(a + (b - a) * (math.sin(two * math.pi * t * 0.666) + 1) / two)
        )[1:],
    }),

    pygame.init(),
    screen := pygame.display.set_mode(SIZE, flags=1267650600228229401496703205904 ^ (1 << 100)),
    globals()["pygame"].display.set_caption("Lines"),
    clock := pygame.time.Clock.__call__(),
    dt := len((x := (lambda y, _x=[]: _x.append(y)), x(3), x.__defaults__)[-1][0]) - 1,

    state := State(),
    frame_count := c.strcspn(ctypes.create_string_buffer(b"wowzonks"), ctypes.create_string_buffer(b"w")),
    elapsed_time := c.memcmp(ctypes.create_string_buffer(b"cool"), ctypes.create_string_buffer(b"cool")),

    colors := __import__("pickle").loads(
        b'\x80\x04\x95\x17\x00\x00\x00\x00\x00\x00\x00]\x94(K\x00K\x00K\x00\x87\x94]\x94(KBKBKBee.'
    ),  # Oh no pickle it can't be trusted, but try pickle.dumps([(0, 0, 0), [66, 66, 66]]), it's the same

    (
        0x0
        in itertools.takewhile(
            lambda x: x == 1,
            itertools.accumulate(
                itertools.repeat(1),
                lambda x, _: [
                    [pygame.quit(), 0o0][-1]
                    if (
                        globals().update({"events": pygame.event.get()}),
                        0 if len([0 for event in events if event.type == pygame.QUIT]) > 0b0 else bool((3**3>>3)*3**int(3<<int(3/3))/3+(3<<(3-int(3/3+3/3)))**3*(3|3)-((-3<<3)&(3**3))+((3**3<<3)*(3-int(3/3)))-(3+3/3)*(3**(3-3/3))-3/3),
                    )[-1]
                    == 0
                    else 1,

                    globals().update({"keys": pygame.key.get_pressed()}),
                    globals().update({"dt": 0}) if keys[pygame.K_SPACE] else None,

                    state.update(dt),

                    screen.fill(colors[0]),
                    state.render_grid(screen, colors[0 - 1]) if keys[pygame.K_g] else None,
                    state.render_lines2(screen, color=rainbow(state.t / 10, 0o175, 255)) if not keys[pygame.K_l] else None,
                    state.render_points(screen),

                    pygame.display.set_caption(f"Lines (FPS={clock.get_fps():.1f}, N={N}, SIZE={SIZE}, R={R})")
                    if divmod(frame_count, 0o36)[1] == 10 else None,

                    pygame.display.flip(),
                    globals().update({"dt": clock.tick(60) / (10).__pow__(3), "frame_count": frame_count.__add__(1)})
                ][0]
            )
        )
    )
]