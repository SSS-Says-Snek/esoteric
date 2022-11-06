_ = [
    globals().clear(),
    globals().setdefault("__builtins__", __import__("builtins")),
    (
        globals().setdefault(
            "modules",
            [
                globals().setdefault(
                    "list_thingy", type("List", (list,), {"__str__": lambda self: "list_thingy"})()
                ),
                globals().setdefault(
                    "new_function",
                    lambda inside_code, args=(): eval(
                        f"lambda {','.join(map(str, args)) if len(args) > 0 else ''}: __import__('types').FunctionType(compile(inside_code, 'irrelevant.py', 'exec'), dict(globals(), **locals()))()",
                        dict(globals(), **{"inside_code": inside_code}),
                        locals(),
                    ),
                )(
                    "import sys\nlist_thingy.append([__import__('pygame'), __import__('itertools'), __import__('random'), __import__('operator'), __import__('ctypes'), __import__('ctypes').CDLL('msvcrt' if sys.platform == 'win32' else 'libc.dylib' if sys.platform == 'darwin' else 'libc.so.6')])",
                    (list_thingy,),
                )(
                    list_thingy
                ),
            ],
        )
    ),
    globals().update(
        {"pygame": globals()["modules"][0][0][0], "itertools": globals()["modules"][0][0][1], "random": globals()["modules"][0][0][2], "operator": globals()["modules"][0][0][3],
         "ctypes": globals()["modules"][0][0][4], "c": globals()["modules"][0][0][5]}
    ),
    pygame.init(),
    globals().update(
        {
            "screen": pygame.display.set_mode((800, 800)),
            "clock": pygame.time.Clock(),
            "font": pygame.font.SysFont(
                getattr(getattr(pygame, "font"), "get_fonts").__call__()[0], 50
            ),
            "score_font": pygame.font.SysFont(
                getattr(getattr(pygame, "font"), "get_fonts").__call__()[0], 90
            ),
            "s": [
                globals().update({"strbufout": __import__("io").StringIO()}),
                globals().update({"ctx": __import__("contextlib").redirect_stdout(strbufout)}),
                ctx.__enter__(),
                (
                    lambda inside_code, args=(): eval(
                        f"lambda {','.join(map(str, args)) if len(args) > 0 else ''}: __import__('types').FunctionType(compile(inside_code, 'irrelevant.py', 'exec'), dict(globals(), **locals()))()",
                        dict(globals(), **{"inside_code": inside_code}),
                        locals(),
                    )
                )(
                    """import ctypes, sys\nstrbuf = ctypes.create_string_buffer(100)\nctypes.CDLL("msvcrt" if sys.platform == "win32" else "libc.dylib" if sys.platform == "darwin" else "libc.so.6").sprintf(strbuf, int.to_bytes(__import__('functools').reduce(lambda x,y:x*2+y,map(int,__import__('struct').unpack(f"<{'?'*31}", b'\\x01\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x01\\x01\\x01\\x01\\x00\\x01\\x00\\x00\\x01\\x01\\x01\\x00\\x00\\x01\\x00\\x00\\x00\\x01\\x01\\x01'))),4,'big'))\nprint(strbuf.value.decode())"""
                )(),
                ctx.__exit__(*__import__("sys").exc_info()),
                strbufout.getvalue(),
            ][-1][:-1],
            "horiz_borders": (pygame.Rect((c.atoi(b"Big chungus"),) * 2, (800, 1)), globals().__getitem__("pygame").Rect(*[(1913420800 >> (i * 10)) & 0b0000000000000000000001111111111 for i in range(4)])),
            "paddle1": pygame.Rect(*[(351933560 >> (i * 8)) & 0xFF for i in range(4)][::-1]),
            "paddle2": pygame.Rect(*__import__('struct').unpack("<HBBB", b'\xf8\x02\xfa\x14x')),
            "ball": [
                globals().update({"fourhundred": ((True + True) << (True << (True << True) + True)) - (True << (True << (True + True)) + True + True) - ((((True + True) << True) - True) << (True + True + True + True))}),
                pygame.Rect((fourhundred,) * 2, (__import__('math').sqrt(fourhundred),) * (True << True))
            ][1],
            "ballv": pygame.Vector2(*[
                globals().update({"a": ctypes.c_int(), "b": ctypes.c_int()}),
                c.sscanf(int.to_bytes(3416115, 3, "big"), int.to_bytes(451594447141, 5, "little"), ctypes.byref(a), ctypes.byref(b)),
                a.value, b.value
            ][-2:]),
            "ballp": pygame.Vector2(*__import__('types').FunctionType((lambda: None).__code__.replace(co_code=b'd\x01S\x00', co_consts=(None, (400,) * 2)), {})()),
            "scores": [c.printf(b"")] * 2,
            "score_y": [
                setattr(c.strchr, "argtypes", [ctypes.c_char_p, ctypes.c_char]),
                setattr(c.strchr, "restype", ctypes.c_char_p),
                c.strchr(b"Zebra", b"Z")[0]
            ][-1],
            "white": tuple((ctypes.c_ubyte * 3)(*(0xFF,)*3)),
            "width": [
                setattr(c.strchr, "argtypes", [ctypes.c_char_p, ctypes.c_char]),
                setattr(c.strchr, "restype", ctypes.POINTER(ctypes.c_uint)),
                sum([(c.strchr(b'\xf3\xca\xb1\xb2', b'\xf3').contents.value >> i * 8) & 0xFF for i in range(4)])
            ][-1],
            "fps": [
                globals().setdefault("fpsthing", (lambda g: a + b + c + d + e).__code__),
                len(fpsthing.co_names) * fpsthing.co_stacksize * (ctypes.cast(fpsthing.co_varnames[0].encode(), ctypes.POINTER(ctypes.c_int)).contents.value - 97)
            ][1]
        }
    ),
    globals().update({"reset_ball": __import__('types').FunctionType((lambda: None).__code__.replace(co_code=b'd\x01t\x00_\x01d\x01t\x00_\x02d\x00S\x00', co_consts=(None, 400), co_names=('ball', 'x', 'y'), co_stacksize=2), {"ball": ball})}),
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

                    [
                        (
                            setattr(paddle1, "y", paddle1.y + 70 * ((pygame.K_q, pygame.K_a).index(event.key) * 2 - True)) if event.key in (pygame.K_q, pygame.K_a) else
                            setattr(paddle2, "y", paddle2.y + 70 * ((pygame.K_p, pygame.K_l).index(event.key) * 2 - (False ^ True))) if event.key in (pygame.K_p, pygame.K_l)
                            else None,

                            setattr(paddle1, "y", paddle1.y.__mod__(width)),
                            setattr(paddle2, "y", paddle2.y % width)
                        ) if event.type == pygame.KEYDOWN else None
                        for event in events
                    ],
                    __builtins__.getattr(__import__('builtins').getattr(globals().__class__.__getitem__(globals(), "pygame"), "display"), "set_caption")(
                        [
                            globals().setdefault("somethingstrbuf", ctypes.create_string_buffer(100)),
                            c.sprintf(somethingstrbuf, b"Pong: %.3f FPS", ctypes.c_double(type(globals().__getitem__('clock')).get_fps(clock))),
                            somethingstrbuf.value.decode()
                        ][2]
                    ),

                    screen.fill((c.printf(b""),)*3),
                    screen.blit(font.render(s, 1, white), (350, 30)),

                    screen.blit(score_font.render("|", True, white), (400, score_y)),
                    screen.blit(score_font.render(type(scores[0]).__str__(scores[0]), True, white), (130, score_y)),
                    screen.blit(score_font.render(str(scores[1]), True, white), (590, score_y)),

                    setattr(ballp, "x", operator.add.__call__.__call__.__call__.__call__.__call__(ball.x, ballv.x)),

                    setattr(ballp, "y", int.__add__(type(ball.y)(ballv.y), type(ball.y)(ball.y))),

                    setattr(ball, "x", round(ballp.x)),
                    setattr(ball, "y", ballp.y.__round__().__round__().__round__().__round__()),

                    setattr(ballv, "y", -ballv.y) if any(map(ball.colliderect, horiz_borders)) else None,
                    [
                        setattr(ballv, "x", -ballv.x),
                        setattr(ballv, "y", random.choice((random.uniform(-8, -5), random.uniform(5, 8))))
                    ] if any(map(ball.colliderect, (paddle1, paddle2))) else [
                        (operator.setitem(scores, 1, scores[1] + 1), reset_ball()) if ball.x < 20 else
                        (operator.setitem(scores, 0, scores[0] + 1), reset_ball()) if ball.x > width - 20
                        else None
                    ],

                    pygame.draw.rect(screen, white, paddle1),
                    pygame.draw.rect(screen, white, paddle2),
                    pygame.draw.rect(screen, white, ball),
                    pygame.display.update(),
                    clock.tick(fps),
                ][0],
            ),
        )
    ),
]