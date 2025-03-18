from pytorch.distributed.tensor.experimental._attention import customized_ops
# from pytorch.distributed._tensor.experimental._attention import customized_ops

customized_ops[
    "aten._scaled_dot_product_fused_attention_overrideable.default"
] = 5
customized_ops[
    "aten._scaled_dot_product_fused_attention_overrideable_backward.default"
] = 6
print(f"torch_mlu::_attention {id(customized_ops)} >>>>>>>>>>>>>>>>>>  {customized_ops}")

