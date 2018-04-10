# ReceiptRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Уникальный идентификатор транзакции в системе клиента, для избежания повторной регистрации чека | 
**type** | **str** |  | 
**client** | [**ReceiptClient**](ReceiptClient.md) |  | 
**items** | [**list[ReceiptItems]**](ReceiptItems.md) | Позиции в чеке | 
**taxes** | [**Taxes**](Taxes.md) |  | [optional] 
**total** | **float** | Итоговая сумма чека, коп. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


