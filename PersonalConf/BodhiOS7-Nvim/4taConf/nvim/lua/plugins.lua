vim.cmd(
    [[
        augroup packer_user_config
	        autocmd!
	        autocmd BufWritePost plugins.lua source <afile> | PackerCompile
	    augroup end
    ]]
)

vim.cmd [[packadd packer.nvim]]

return require('packer').startup(
    function() 
        use 'wbthomason/packer.nvim'
	    use{
	        'nvim-telescope/telescope.nvim',
	        requires = {{'nvim-lua/plenary.nvim'}}
	    }
	    use{
	        'nvim-treesitter/nvim-treesitter',
	        run = ':TSUpdate'
        }
	    use 'nvim-treesitter/playground'
        use{
            'williamboman/nvim-lsp-installer',
            'neovim/nvim-lspconfig'
        }
        use{
            'hrsh7th/nvim-cmp',
            requires = {
                'hrsh7th/cmp-nvim-lsp',
                'hrsh7th/cmp-buffer',
                'hrsh7th/cmp-path',
                'hrsh7th/cmp-cmdline'
            }
        }
        use 'EdenEast/nightfox.nvim'
        use 'feline-nvim/feline.nvim' --Mejorar apariencia visual de Nvim
        use 'kyazdani42/nvim-web-devicons' --Mejorar la apariencia de Nvim
    end
)
