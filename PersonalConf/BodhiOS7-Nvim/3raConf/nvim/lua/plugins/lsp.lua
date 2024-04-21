return{
    'neovim/nvim-lspconfig',
    dependencies = {
        'williamboman/mason.nvim',
        'folke/neodev.nvim' -- simplifies Lua languaje configuration.
    },
    config = function()
        local on_attach = function(_, bufnr) 
            vim.bo[bufnr].omnifunc = 'v:lua.vim.lsp.omnifunc'
        end
        -- for Lua languaje
        require('neodev').setup()
        require('lspconfig').lua_ls.setup({
            on_attach = on_attach,
            settings = {
                Lua = {
                    telemetry = {enable = false},
                    workspace = {checkThirdParty = false}
                }
            }
        })
    end
}
