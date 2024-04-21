return{
    'nvim-treesitter/nvim-treesitter',
    build = ':TSUpdate',
    event = 'VeryLazy',
    main = 'nvim-treesitter.configs',
    opts = {
        ensure_installed = {
            'lua', 'luadoc', 
            'php', 'phpdoc',
            'python', 
            'javascript', 'html', 'css',
            'json','sql', 'dockerfile'
        },
        highlight = {enable = true},
        indent = {enable = true}
    }
}
