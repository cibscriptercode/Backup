vim.opt.guicursor = '' -- Cursor grueso
vim.opt.mouse = 'a'

-- numeros relativos
vim.opt.nu = true
vim.opt.relativenumber = true

-- 2 tabs
vim.opt.tabstop = 2
vim.opt.softtabstop = 2
vim.opt.shiftwidth = 2
vim.opt.expandtab = true

vim.opt.smartindent = true

vim.opt.clipboard = 'unnamedplus' -- Copiar al portapapeles del SO

vim.opt.wrap = false -- Sin limite de la longitud de la linea

-- Cuando busca no se queda con color y mientras busca se pone de color
vim.opt.hlsearch = false
vim.opt.incsearch = true

-- Para mejorar los colores
vim.opt.termguicolors = true

-- El cursor simpre queda con 8 espacios para arriba y para abajo
vim.opt.scrolloff = 8
vim.opt.signcolumn = 'yes'
vim.opt.isfname:append('@-@')
