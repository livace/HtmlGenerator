class Element:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.body = args
        self.attrs = kwargs

    def __call__(self, *args, **kwargs):
        return Element(self.name, *[*self.body, *args], **{**self.attrs, **kwargs})

    def format_attrs(self):
        if self.attrs:
            return ' '.join('{key}={value}'.format(key=key, value=value)
                            for (key, value) in zip(self.attrs.keys(), self.attrs.values()))
        else:
            return None

    def format_body(self):
        if self.body:
            return ''.join([element if isinstance(element, str) else element.__repr__() for element in self.body])
        else:
            return None

    def __repr__(self):
        attrs = self.format_attrs() or ''
        body = self.format_body()
        if body:
            return '<{name} {attrs}>{body}</{name}>'.format(name=self.name, attrs=attrs, body=body)
        else:
            return '<{name} {attrs} />'.format(name=self.name, attrs=attrs)

Html = Element('html')
Body = Element('body')
Div = Element('div')
A = Element('a')
Br = Element('br')

print(
    Html(
        Body(
            Div(id=1337)(
                Div(
                    'hi'
                ),
                'text',
                Br,
                A(href='https://vk.com')(
                    'vk'
                )
            )
        )
    )
)