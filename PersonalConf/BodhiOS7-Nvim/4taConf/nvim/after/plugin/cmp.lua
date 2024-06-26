local cmp = require 'cmp'

cmp.setup(
    {
        snippet = {expand = function(args) end},
        window = {},
        mapping = cmp.mapping.preset.insert(
            {
                ['<C-b>'] = cmp.mapping.scroll_docs(-4),
                ['<C-f>'] = cmp.mapping.scroll_docs(4),
                ['<C-Space>'] = cmp.mapping.complete(),
                ['<C-e>'] = cmp.mapping.abort,
                ['<C-y>'] = cmp.mapping.confirm({select = true})
            }
        ),
        sources = cmp.config.sources(
            {{name = 'nvim_lsp'}},
            {{name = 'buffer'}}
        )
    }
)

cmp.setup.cmdline(
    '/',
    {
        mapping = cmp.mapping.preset.cmdline(),
        sources = cmp.config.sources(
            {{name = 'path'}},
            {{name = 'cmdline'}}
        )
    }
)


