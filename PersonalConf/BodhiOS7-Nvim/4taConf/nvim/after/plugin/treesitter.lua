require 'nvim-treesitter.configs'.setup{
    ensure_installed = {'python', 'lua', 'bash', 'sql', 'javascript', 'c', 'json', 'dockerfile', 'gitignore'},
    sync_install = false,
    auto_install = true,
    ignore_install = {},
    highlight ={
        enable = true,
	    additional_vim_regex_highlighting = false
    }
}