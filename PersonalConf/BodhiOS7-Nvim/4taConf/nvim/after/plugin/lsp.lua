require('nvim-lsp-installer').setup{automatic_instalation =true}


local opts = {noremap = true, silent = true}

vim.keymap.set('n', '<space>e', vim.diagnostic.open_float, opts)
vim.keymap.set('n', '[d', vim.diagnostic.goto_prev, opts)
vim.keymap.set('n', ']d', vim.diagnostic.goto_next, opts)
vim.keymap.set('n', '<space>q', vim.diagnostic.setloclist, opts)

local on_attach = function(client, bufnr)
    vim.api.nvim_buf_set_option(bufnr, 'omnifunc', 'v:lua.vim.lsp.omnifunc')
    local bufopts = {noremap = true, buffer = bufnr}
    vim.keymap.set('n', 'gD', vim.lsp.buf.declaration, bufopts)
    vim.keymap.set('n', 'gd', vim.lsp.buf.definition, bufopts)
    vim.keymap.set('n', 'k', vim.lsp.buf.hover, bufopts)
    vim.keymap.set('n', 'gi', vim.lsp.buf.implementation, bufopts)
    vim.keymap.set('n', '<C-k>', vim.lsp.buf.signature_help, bufopts)
    vim.keymap.set('n', '<space>wa', vim.lsp.buf.add_workspace_folder, bufopts)
    vim.keymap.set('n', '<space>wr', vim.lsp.buf.remove_workspace_folder, bufopts)
    vim.keymap.set(
        'n', '<space>wl', 
        function () print(vim.inspect(vim.lsp.buf.list_workspace_folders())) end,
        bufopts
    )
    vim.keymap.set('n', '<space>D', vim.lsp.buf.type_definition, bufopts)
    vim.keymap.set('n', '<space>nr', vim.lsp.buf.rename, bufopts)
    vim.keymap.set('n', '<space>ca', vim.lsp.buf.code_action, bufopts)
    vim.keymap.set('n', 'gr', vim.lsp.buf.references, bufopts)
    vim.keymap.set('n', '<space>f', vim.lsp.buf.formatting, bufopts)
end

local lsp_flags = {debounce_text_changes = 150}
local lspconfig = require('lspconfig')

lspconfig.lua_ls.setup{
    on_attach = on_attach,
    flags = lsp_flags,
    settings = {
        Lua = {
            runtime = {version = 'LuaJIT'},
            diagnostics = {globals = {'vim'}},
            workspace = {library = vim.api.nvim_get_runtime_file('', true)},
            telemetry = {enable = false}
        }
    }
}

lspconfig.pyright.setup{
    on_attach = on_attach,
    flags = lsp_flags,
    settings = {
        python = {
            analysis = {
                autoSearchPaths = true,
                diagnosticMode = 'workspace',
                useLibraryCodeForTypes = true
            }
        }
    }
}

lspconfig.bashls.setup{
    on_attach = on_attach,
    flags = lsp_flags
}

lspconfig.sqlls.setup{
    on_attach = on_attach,
    flags = lsp_flags
}
