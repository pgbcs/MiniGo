.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final b Ljava/lang/String; = "hello world"

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	getstatic MiniGoClass/b Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
Label3:
	nop
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
