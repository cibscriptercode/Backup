require('telescope').setup{
    defaults = {
        mappings = {
	   i = {['<C-h>'] = 'wich_key'}
	}
    },
    pickers = {},
    extensions = {}
}

vim.keymap.set('n', '<leader>pp', require 'telescope.builtin'.find_files, {remap = false})
