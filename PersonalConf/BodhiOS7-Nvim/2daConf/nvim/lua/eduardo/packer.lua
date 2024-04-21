-- ejecutar :wq, :so, :PackerSync --> Para instalacion de plugins
vim.cmd [[packadd packer.vim]]

return require('packer').startup(
    function(use)
        use 'wbthomason/packer.nvim'
	use {
	    'nvim-telescope/telescope.nvim', 
	    tag = '0.1.2',
	    requires = {{'nvim-lua/plenary.nvim'}}
	}
	use {'rose-pine/neovim', as = 'rose-pine'}
	use {
	    'nvim-treesitter/nvim-treesitter',
	    run =
	        function()
		    local ts_update = require('nvim-treesitter.install').update({with_sync = true})
		    ts_update()
		end
	}
	use('theprimeagen/harpoon')
	use('prettier/vim-prettier') -- Luego de su instalacion, ejecutar 'npm i -g prettier' en '.config/nvim/'
	use{
	    'VonHeikemen/lsp-zero.nvim',
	    branch = 'v2.x',
	    requires = {
	        {'neovim/nvim-lspconfig'},
		{
		    'williamboman/mason.nvim',
		    run = 
		        function()
			    pcall(vim.cmd, 'MasonUpdate')
			end
		},
		{'williamboman/mason-lspconfig.nvim'},
		{'hrsh7th/nvim-cmp'},
		{'hrsh7th/cmp-nvim-lsp'},
		{'L3MON4D3/LuaSnip'}
	    }
	}
    end
)
