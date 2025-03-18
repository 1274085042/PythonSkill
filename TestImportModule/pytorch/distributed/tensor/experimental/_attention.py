from typing import Generator

customized_ops = {
    "aten._scaled_dot_product_flash_attention.default": 1,
    "aten._scaled_dot_product_flash_attention_backward.default": 2,
    "aten._scaled_dot_product_efficient_attention.default": 3,
    "aten._scaled_dot_product_efficient_attention_backward.default": 4,
}
print(f"torch::_attention {id(customized_ops)} >>>>>>>>>>>>>>>>>>  {customized_ops}")

def context_parallel(
    mesh,
    buffers,
    buffer_seq_dims,
    no_restore_buffers,
) -> Generator[None, None, None]:

    buffers = [] if buffers is None else buffers
    buffer_seq_dims = [] if buffer_seq_dims is None else buffer_seq_dims
    no_restore_buffers = set() if no_restore_buffers is None else no_restore_buffers

