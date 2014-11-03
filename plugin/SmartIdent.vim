if !has('python')
    finish
endif

function! SmartIdent()
    :python import sys, vim
    :python sys.argv = ['', vim.current.buffer.name]

    :python import smartident_vim

endfunction

augroup smartident
    autocmd! FileType * call SmartIdent#Setup()
augroup END
