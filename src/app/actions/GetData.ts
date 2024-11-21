import { createClient } from "@/lib/server";

export async function Get({
  limit,
  offset,
}: {
  limit: number;
  offset: number;
}) {
  const supabase = await createClient();

  const { data, error } = await supabase
    .from("colors")
    .select("*")
    .range(offset, offset + limit - 1); // جلب البيانات من offset إلى offset + limit - 1

  if (error) {
    throw new Error(error.message);
  }

  return data;
}
