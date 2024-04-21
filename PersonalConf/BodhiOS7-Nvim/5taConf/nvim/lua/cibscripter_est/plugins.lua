vim.cmd([[
    augroup packer_user_config
        autocmd!
        autocmd BufWritePost plugins.lua source <afile> | PackerCompile
    augroup end
]])

vim.cmd [[packadd packer.nvim]]

return require('packer').startup(function()
    use 'wbthomason/packer.nvim' -- Gestor de plugins.

    use 'ellisonleao/gruvbox.nvim' -- Esquema de color.

    use 'feline-nvim/feline.nvim' -- Cambia la aperiencia visual del editor.
    use 'kyazdani42/nvim-web-devicons'

    use 'jiangmiao/auto-pairs' -- Insertar o eliminar corchetes, paréntesis, comillas en pares.

    use 'preservim/nerdtree' -- Explorador de sistemas de archivos.

    use {'neoclide/coc.nvim', branch = 'release'} -- Auto-completado de código.
end)
